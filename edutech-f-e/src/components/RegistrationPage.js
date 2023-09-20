import React, { useState } from 'react';
import axios from 'axios';

const RegistrationPage = () => {
    const [learnerName, setLearnerName] = useState('');
    const [learnerEmail, setLearnerEmail] = useState('');

    const registerLearner = async () => {
	try {
	    const response = await axios.post('http://localhost:8080/learners', { name: learnerName, email: learnerEmail });
	    console.log(response.data);
	} catch (error) {
	    console.error(`Error registering learner: ${error}`);
	}
    };

    return (
	<div>
	    <h2>Registration Page</h2>
	    <input type="text" value={learnerName} onChange={(e) => setLearnerName(e.target.value)} placeholder="Learner Name" />
	    <input type="text" value={learnerEmail} onChange={(e) => setLearnerEmail(e.target.value)} placeholder="Learner Email" />
	    <button onClick={registerLearner}>Register</button>
	</div>
    );
};

export default RegistrationPage;
