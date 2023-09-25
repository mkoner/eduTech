import React, { useState } from 'react';
import './Login.css';

function Login() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = event => {
	event.preventDefault();

	fetch('/learners/login', {
	    method: 'POST',
	    headers: {
		'Content-Type': 'application/json',
	    },
	    body: JSON.stringify({ email, password }),
	})
	    .then(response => response.json())
	    .then(data => {
		if (data.message === 'Login successful') {
		    // Handle successful login here
		    // For example, you might store the user's ID in local storage
		    localStorage.setItem('userId', data.user);
		} else {
		    // Handle failed login here
		    // For example, you might display an error message
		    alert(data.message);
		}
	    });
    };

    return (
	<form onSubmit={handleSubmit}>
	    <label>
		Email:
		<input type="email" value={email} onChange={e => setEmail(e.target.value)} required />
	    </label>
	    <label>
		Password:
		<input type="password" value={password} onChange={e => setPassword(e.target.value)} required />
	    </label>
	    <button type="submit">Log in</button>
	</form>
    );
}

export default Login;