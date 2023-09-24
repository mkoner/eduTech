import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Courses.css';

const Courses = () => {
    const [courses, setCourses] = useState([]);
    const [courseName, setCourseName] = useState('');
    const [description, setDescription] = useState('');
    const [selectedCourse, setSelectedCourse] = useState(null);

    useEffect(() => {
	fetchCourses();
    }, []);

    const fetchCourses = () => {
	axios.get('/api/courses')
	    .then(response => {
		setCourses(response.data.data);
	    })
	    .catch(error => {
		console.error('There was an error!', error);
	    });
    };

    const handleSubmit = (event) => {
	event.preventDefault();

	const course = {
	    course_name: courseName,
	    description: description
	};

	if (selectedCourse) {
	    axios.put(`/api/courses/${selectedCourse.id}`, course)
	        .then(response => {
		    fetchCourses();
		})
	        .catch(error => {
		    console.error('There was an error!', error);
		});
	} else {
	    axios.post('/api/courses', course)
	        .then(response => {
		    fetchCourses();
		})
	        .catch(error => {
		    console.error('There was an error!', error);
		});
	}
    };

    const handleUpdate = (course) => {
	setSelectedCourse(course);
	setCourseName(course.course_name);
	setDescription(course.description);
    };

    const handleDelete = (id) => {
	axios.delete(`/api/courses/${id}`)
	    .then(response => {
		fetchCourses();
	    })
	    .catch(error => {
		console.error('There was an error!', error);
	    });
    };

    return (
	<div>
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
	    <div>
		{courses.map((course, index) => (
		    <div key={index}>
			<h2>{course.course_name}</h2>
			<p>{course.description}</p>
			<button onClick={() => handleUpdate(course)}>Update</button>
			<button onClick={() => handleDelete(course.id)}>Delete</button>
		    </div>
		))}
	    </div>
	</div>
	    );
};

export default Courses;
