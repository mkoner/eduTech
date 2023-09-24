import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AdminList.css';
import { fetchAdmins } from '../../api';

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
	const {firstName, lastName, email, phoneNumber, page} = filters;

	const handleChange = (evt) => {
		const { name, value } = evt.target;
		setFilters((prevState) => ({
		  ...prevState,
		  [name]: value,
		}))
	  }

    useEffect(() => {
	getAdmins()
    }, []); 

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
				  <tr>
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
					<td name="id" value={id} onChange={handleChange}></td>
					<td name="firstName" value={firstName} onChange={handleChange}></td>
					<td name="lastName" value={lastName} onChange={handleChange}></td>
					<td name="email" value={email} onChange={handleChange}></td>
					<td name="phoneNumber" value={phoneNumber} onChange={handleChange}></td>
					<td></td>
					</tr>
				  {admins.data.map((user) => (
					<tr key={user.id}>
					  <td>{user.id}</td>
					  <td>{user.first_name}</td>
					  <td>{user.lastst_name}</td>
					  <td>{user.email}</td>
					  <td>{user.phone_number}</td>
					  <td>{user.is_active}</td>
					</tr>
				  ))}
				</tbody>
			  </table>
		} 
	</div>
    );
};

export default AdminList;
