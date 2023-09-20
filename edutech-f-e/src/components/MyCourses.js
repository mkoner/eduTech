// MyCourses.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MyCourses = () => {
    const [courses, setCourses] = useState([]);

    useEffect(() => {
	// Replace with your actual API endpoint
	axios.get('http://localhost:8080/learners/:id/courses')
	    .then(response => {
		setCourses(response.data);
	    })
	    .catch(error => {
		console.error(`Error fetching courses: ${error}`);
	    });
    }, []);

    return (
	<div>
	    <h2>My Courses</h2>
	    {courses.map(course => (
		<div key={course.id}>
		    <h3>{course.name}</h3>
		    {/* Add more course details here */}
		</div>
	    ))}
	</div>
	    );
};

export default MyCourses;
