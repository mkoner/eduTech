import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CourseMaterials = () => {
    const [courseMaterials, setCourseMaterials] = useState([]);
    const [materialTitle, setMaterialTitle] = useState('');
    const [materialSource, setMaterialSource] = useState('');
    const [materialAuthor, setMaterialAuthor] = useState('');
    const [materialLink, setMaterialLink] = useState('');

    useEffect(() => {
	getCourseMaterials();
    }, []);

    const getCourseMaterials = async () => {
	try {
	    const response = await axios.get('/api/coursematerials');
	    setCourseMaterials(response.data);
	} catch (error) {
	    console.error(`Error fetching course materials: ${error}`);
	}
    };

    const addCourseMaterial = async () => {
	try {
	    const response = await axios.post('/api/coursematerials', { title: materialTitle, source: materialSource, author: materialAuthor, link: materialLink });
	    setCourseMaterials([...courseMaterials, response.data]);
	} catch (error) {
	    console.error(`Error adding course material: ${error}`);
	}
    };

    return (
	<div>
	    <h1>Course Material List</h1>
	    {courseMaterials.map((material) => (
		<div key={material.id}>
		    <h2>{material.title}</h2>
		    <p>{material.source}</p>
		    <p>{material.author}</p>
		    <a href={material.link}>Link to Material</a>
		</div>
	    ))}
	    <input type="text" value={materialTitle} onChange={(e) => setMaterialTitle(e.target.value)} placeholder="Material Title" />
	    <input type="text" value={materialSource} onChange={(e) => setMaterialSource(e.target.value)} placeholder="Material Source" />
	    <input type="text" value={materialAuthor} onChange={(e) => setMaterialAuthor(e.target.value)} placeholder="Material Author" />
	    <input type="text" value={materialLink} onChange={(e) => setMaterialLink(e.target.value)} placeholder="Material Link" />
	    <button onClick={addCourseMaterial}>Add Course Material</button>
	</div>
	    );
};

export default CourseMaterials;
