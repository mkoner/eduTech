import React, { useState } from "react";

const AdminDetailsPage = ({ user }) => {
  const [admin, setAdmin] = useState({
    firstName: user.first_name,
    lastName: user.last_name,
    email: user.email,
    phoneNumber: user.phone_number,
    password:'',
    isActive: user.is_active,
  });

  const {firstName, lastName, email, phoneNumber, password, isActive} = admin;

  const handleChange = (evt) => {
    const { name, value } = evt.target;
    setAdmin((prevState) => ({
      ...prevState,
      [name]: value,
    }))
  }

  const handleSubmit = (event) => {
    event.preventDefault();

    // Update the user details on the server
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={firstName}
        onChange={handleChange}
      />
      <input
        type="email"
        name="email"
        placeholder="Email"
        value={email}
        onChange={handleChange}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default AdminDetailsPage;