import React from 'react';

const UsersTable = ({ users }) => {
  return (
      <>
        {users.map((user) => (
			<tr key={user.id}>
            <td>{user.id}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
            <td>{user.phone_number}</td>
            <td> <input type="checkbox" name="isActive" defaultChecked={user.is_active}/></td>
            </tr>
        ))}
      </>
  );
};

export default UsersTable;