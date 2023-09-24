import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

function Header() {
    return (
	<header className="header">
	    <h1>EduTech</h1>
	    <nav>
		<Link to="/admins">Admins</Link>
		<Link to="/learners">Learners</Link>
		<Link to="/courses">Courses</Link>
		<Link to="/course-materials">Course Materials</Link>
	    </nav>
	</header>
    );
}

export default Header;

