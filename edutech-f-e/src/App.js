import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Admin from './components/Admins';
import Learners from './components/Learners';
import CourseMaterials from './components/CourseMaterials';
import Courses from './components/Courses';
import HomePage from './components/HomePage';
import Login from './components/Login';
import AdminList from './pages/adminList/AdminList';

const App = () => {
    return (
	<Router>
	    <div>
		<nav className="navbar navbar-expand-lg navbar-light bg-light">
		    <div className="container-fluid">
			<ul className="navbar-nav me-auto mb-2 mb-lg-0">
			    <li className="nav-item"><Link className="nav-link" to="/admins">Admin</Link></li>
			    <li className="nav-item"><Link className="nav-link" to="/learners">Learners</Link></li>
			    <li className="nav-item"><Link className="nav-link" to="/course-materials">Course Materials</Link></li>
			    <li className="nav-item"><Link className="nav-link" to="/courses">Courses</Link></li>
			</ul>
		    </div>
		</nav>
		<Routes>
		    <Route path="/" element={<HomePage />} />
		    <Route path="/admins" element={<AdminList />} />
		    <Route path="/login" element={<Login />} />
		    <Route path="/learners/*" element={<Learners />} />
		    <Route path="/course-materials" element={<CourseMaterials />} />
		    <Route path="/courses" element={<Courses />} />
		</Routes>
	    </div>
	</Router>
    );
};

export default App;
