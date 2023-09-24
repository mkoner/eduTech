import React from 'react';
import './Learners.css';

class Learners extends React.Component {
    constructor(props) {
	super(props);
	this.state = {
	    learners: []
	};
    }

    componentDidMount() {
	fetch('/learners/')
	    .then(response => response.json())
	    .then(data => this.setState({ learners: data }));
    }

    render() {
	return (
	    <div className="learners">
		<h1 className="title">Learners</h1>
		{this.state.learners.map((learner, index) => (
		    <div key={index} className="learner">
			<h2 className="name">{learner.first_name} {learner.last_name}</h2>
			<p className="description">Email: {learner.email}</p>
			<p className="description">Phone Number: {learner.phone_number}</p>
		    </div>
		))}
	    </div>
	);
    }
}

export default Learners;
