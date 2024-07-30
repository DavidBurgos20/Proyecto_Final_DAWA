import React, { useState, useEffect } from 'react';
import { List, ListItem, ListItemAvatar, Avatar, ListItemText, IconButton } from '@mui/material';
import { Delete } from '@mui/icons-material';
import { getAmigos, deleteAmigo } from '../../Capa_Datos/authService';

function AmigosComponent() {
  const [amigos, setAmigos] = useState([]);

  useEffect(() => {
    const fetchAmigos = async () => {
      try {
        const data = await getAmigos();
        setAmigos(data);
      } catch (error) {
        console.error('Failed to fetch friends:', error);
      }
    };

    fetchAmigos();
  }, []);

  const handleDeleteFriend = async (amigoId) => {
    try {
      await deleteAmigo(amigoId);
      setAmigos(amigos.filter((amigo) => amigo.id !== amigoId));
    } catch (error) {
      console.error('Failed to delete friend:', error);
      alert('Failed to delete friend.');
    }
  };

  return (
    <List>
      {amigos.map((amigo) => (
        <ListItem key={amigo.id}>
          <ListItemAvatar>
            <Avatar src={amigo.avatar} />
          </ListItemAvatar>
          <ListItemText primary={amigo.username} />
          <IconButton edge="end" aria-label="delete" onClick={() => handleDeleteFriend(amigo.id)}>
            <Delete />
          </IconButton>
        </ListItem>
      ))}
    </List>
  );
}

export default AmigosComponent;
