import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [users, setUsers] = useState([]);

  const getUsers = async () => {
    const res = await axios.get("http://IP-DE-SERVICIO-READ/users");
    setUsers(res.data.users);
  };

  useEffect(() => {
    getUsers();
  }, []);

  return (
    <div>
      <h1>Usuarios</h1>
      <ul>
        {users.map(u => (
          <li key={u.id}>{u.name} - {u.email}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
