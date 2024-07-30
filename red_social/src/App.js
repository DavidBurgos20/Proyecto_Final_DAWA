import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import './App.css';
import 'semantic-ui-css/semantic.min.css'
import Login from '../src/Capa_presentacion/inicio/login.jsx';
import Feed from '../src/Capa_presentacion/inicio/feed.jsx';
import Perfil from '../src/Capa_presentacion/inicio/perfil.jsx';
import Navbar from '../src/Capa_presentacion/inicio/Navbar.jsx';
import Post from '../src/Capa_presentacion/inicio/post.jsx';
import CrearUsuario from '../src/Capa_presentacion/inicio/CrearUsuario.jsx';
import FriendRequests from '../src/Capa_presentacion/inicio/FriendRequestDialog.jsx'; // Importar el nuevo componente

function App() {
  const [postDialogOpen, setPostDialogOpen] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);

  const handlePostDialogOpen = () => {
    setPostDialogOpen(true);
  };

  const handlePostDialogClose = () => {
    setPostDialogOpen(false);
  };

  const handleLogin = (userData) => {
    setIsAuthenticated(true);
    setUser(userData); // Set the logged-in user data
    console.log("User data after login:", userData); // Verificar los datos del usuario
  };

  const handleLogout = () => {
    setIsAuthenticated(false);
    setUser(null); // Clear the user data on logout
  };

  return (
    <Router>
      <div className="App">
        {isAuthenticated && (
          <Navbar
            onCreatePost={handlePostDialogOpen}
            onLogout={handleLogout}
            currentUserId={user?.id} // Pass currentUserId as a prop
          />
        )}
        <Routes>
          <Route path="/" element={<Login onLogin={handleLogin} />} />
          <Route path="/register" element={<CrearUsuario />} />
          <Route path="/feed" element={isAuthenticated ? <Feed userId={user?.id} /> : <Navigate to="/" />} />
          <Route path="/profile" element={isAuthenticated ? <Perfil userId={user?.id} /> : <Navigate to="/" />} />
          <Route path="/friendrequests" element={isAuthenticated ? <FriendRequests userId={user?.id} /> : <Navigate to="/" />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
        {isAuthenticated && (
          <Post 
            open={postDialogOpen} 
            onClose={handlePostDialogClose} 
            onCreatePost={() => {}} 
            userId={user?.id} // Pasar userId a Post
          />
        )}
      </div>
    </Router>
  );
}

export default App;

