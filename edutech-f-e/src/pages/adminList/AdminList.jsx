import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './AdminList.css';
import { fetchAdmins } from '../../api';

const AdminList = () => {
    const [admins, setAdmins] = useState([]);

    useEffect(() => {
	getAdmins()
    }, []);

    const getAdmins = async () => {
        console.log('get admins called')
	try {
	    const response = fetchAdmins();
        console.log(response)
	    //setAdmins(response.data);
	} catch (error) {
	    console.error(`Error fetching admins: ${error}`);
	}
    };

    return (
	<div className="admin-container">
	   <h1>Admin Users</h1>
	    {admins.map(admin => (
		<div key={admin.id} className="admin-item">
		    <h2>{admin.first_name} {admin.last_name}</h2>
		    <p>Email: {admin.email}</p>
		    <button onClick={() => handleSelectAdmin(admin)}>Edit</button>
		</div>
	    ))} 
	</div>
    );
};

export default AdminList;
