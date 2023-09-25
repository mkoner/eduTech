import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AdminList.css';
import { fetchAdmins } from '../../api';

import UsersTable from '../../components/usersTable/usersTable';

const AdminList = () => {
    const [admins, setAdmins] = useState([]);
	const [filters, setFilters] = useState({
		id: null,
		firstName: null,
		lastName: null,
		email: null,
		phoneNumber: null,
		page: 1,
	});
	const {id, firstName, lastName, email, phoneNumber, page} = filters;

	const handleChange = (evt) => {
		const { name, value } = evt.target;
		setFilters((prevState) => ({
		  ...prevState,
		  [name]: value,
		}))
	  }

    useEffect(() => {
	getAdmins()
    }, [filters]); 

    const getAdmins = async () => {
        console.log('get admins called')
	let result =  Object.entries(filters).reduce((a,[k,v]) => (v == null ? a : (a[k]=v, a)), {});
	try {
	    const response = await fetchAdmins(result);
	    setAdmins(response.data);
	} catch (error) {
	    console.error(`Error fetching admins: ${error}`);
	}
    };


    return (
	<div className="admin-container">
	   <h1>Admin Users</h1>
	    {admins &&
			    <table className="user-list">
				<thead>
				  <tr className="filter-row">
					<th>Id</th>
					<th>First Name</th>
					<th>Last Name</th>
					<th>Email</th>
					<th>phone number</th>
					<th>is Active</th>
				  </tr>
				</thead>
				<tbody>
				<tr>
					<td><input type="text" name="id" value={id} onChange={handleChange}/></td>
					<td><input type="text" name="firstName" value={firstName} onChange={handleChange}/></td>
					<td><input type="text" name="lastName" value={lastName} onChange={handleChange}/></td>
					<td><input type="text" name="email" value={email} onChange={handleChange}/></td>
					<td><input type="text" name="phoneNumber" value={phoneNumber} onChange={handleChange}/></td>
					<td></td>
				</tr>
				<UsersTable users={admins}/>
				</tbody>
			  </table>
		} 
	</div>
    );
};

export default AdminList;
