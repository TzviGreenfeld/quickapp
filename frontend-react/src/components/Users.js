import React, { useEffect, useState } from "react";
import api from "../api";

const UserComponent = () => {
  const [users, setUsers] = useState([]);
  const [username, setUsername] = useState("");

  // Fetch users on component mount
  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await api.get("/user");
        setUsers(response.data.users);
      } catch (error) {
        console.error("Error fetching users:", error);
      }
    };

    fetchUsers();
  }, []);

  // Handle form submission to add a user
  const addUser = async (event) => {
    event.preventDefault();
    try {
      const response = await api.post("/user", { username });
      setUsers([...users, response.data]);
      setUsername("");
    } catch (error) {
      console.error("Error adding user:", error);
    }
  };

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>

      <form onSubmit={addUser}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Enter username"
          required
        />
        <button type="submit">Add User</button>
      </form>
    </div>
  );
};

export default UserComponent;
