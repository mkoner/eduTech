import React, { useState, useEffect } from 'react';
import './Courses.css';

const Courses = ({ user = { role: 'learner' } }) => {
    const [courses, setCourses] = useState([]);
    const [courseName, setCourseName] = useState('');
    const [description, setDescription] = useState('');
    const [selectedCourse, setSelectedCourse] = useState(null);

    // Mock data
    const mockCourses = [
	{ id: 1, course_name: 'Course 1', description: 'This is course 1' },
	{ id: 2, course_name: 'Course 2', description: 'This is course 2' },
	// Add more courses as needed
    ];

    useEffect(() => {
	// Use mock data instead of fetching from API
	setCourses(mockCourses);
    }, []);

    const handleSubmit = (event) => {
	event.preventDefault();

	const course = {
	    course_name: courseName,
	    description: description
	};

	if (selectedCourse) {
	    console.log(`Updating course ${selectedCourse.id}`);
	    // Replace this with your actual API call
	} else {
	    console.log('Creating new course');
	    // Replace this with your actual API call
	}

	// Clear form
	setCourseName('');
	setDescription('');
	setSelectedCourse(null);
    };

    const handleUpdate = (course) => {
	setSelectedCourse(course);
	setCourseName(course.course_name);
	setDescription(course.description);
    };

    const handleDelete = (id) => {
	console.log(`Deleting course ${id}`);
	// Replace this with your actual API call
    };

    return (
	<div>
	    {user && user.role === 'admin' && (
		<form onSubmit={handleSubmit}>
		    <label>
			Course Name:
			<input
			    type="text"
			    value={courseName}
			    onChange={e => setCourseName(e.target.value)}
			/>
		    </label>
		    <label>
			Description:
			<textarea
			    value={description}
			    onChange={e => setDescription(e.target.value)}
			/>
		    </label>
		    <input type="submit" value={selectedCourse ? 'Update' : 'Submit'} />
		</form>
	    )}
	    <div>
		{courses.map((course, index) => (
		    <div key={index}>
			<h2>{course.course_name}</h2>
			<p>{course.description}</p>
			{user && user.role === 'admin' && (
			    <>
				<button onClick={() => handleUpdate(course)}>Update</button>
				<button onClick={() => handleDelete(course.id)}>Delete</button>
			    </>
			)}
		    </div>
		))}
	    </div>
	</div>
	    );
};

export default Courses;
