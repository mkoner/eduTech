import React from "react";
import './CourseCard.css'

const CourseCard = ({ name, description }) => {
  return (
    <div className="course-card">
      <div className="card-header">
        <h2>{name}</h2>
      </div>
      <div className="card-body">
        <p>{description}</p>
      </div>
    </div>
  );
};

export default CourseCard;