import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Admins.css';

const Admin = () => {
    const [admins, setAdmins] = useState([]);
    const [selectedAdmin, setSelectedAdmin] = useState(null);

    useEffect(() => {
	getAdmins();
    }, []);

    const getAdmins = async () => {
	try {
	    const response = await axios.get('/admins');
	    setAdmins(response.data);
	} catch (error) {
	    console.error(`Error fetching admins: ${error}`);
	}
    };

    const handleSelectAdmin = (admin) => {
	setSelectedAdmin(admin);
    };

    const handleUpdateAdmin = (updatedAdmin) => {
	axios.put(`/admins/${updatedAdmin.id}`, updatedAdmin)
	    .then(response => {
		setAdmins(admins.map(admin => admin.id === updatedAdmin.id ? updatedAdmin : admin));
		setSelectedAdmin(null);
	    });
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
	    {selectedAdmin && (
		<div className="admin-form">
		    <h2>Edit Admin</h2>
		    <form onSubmit={(e) => { e.preventDefault(); handleUpdateAdmin(selectedAdmin); }}>
			<label>
			    First Name:
			    <input type="text" value={selectedAdmin.first_name} onChange={(e) => setSelectedAdmin({ ...selectedAdmin, first_name: e.target.value })} />
			</label>
			<label>
			    Last Name:
			    <input type="text" value={selectedAdmin.last_name} onChange={(e) => setSelectedAdmin({ ...selectedAdmin, last_name: e.target.value })} />
			</label>
			<label>
			    Email:
			    <input type="email" value={selectedAdmin.email} onChange={(e) => setSelectedAdmin({ ...selectedAdmin, email: e.target.value })} />
			</label>
			{/* Add other fields as necessary */}
			<button type="submit">Save Changes</button>
		    </form>
		</div>
		    )}
	</div>
    );
};

export default Admin;
