import React, { useState, useEffect } from 'react';
import { Dialog, DialogTitle, DialogContent, DialogActions, Button, List, ListItem, ListItemAvatar, Avatar, ListItemText, Typography } from '@mui/material';
import { getUsers, createFriendRequest, getFriendRequests, updateFriendRequest } from '../../Capa_Datos/authService';

function FriendRequestDialog({ open, onClose, currentUserId }) {
  const [users, setUsers] = useState([]);
  const [friendRequests, setFriendRequests] = useState([]);
  const [selectedUserId, setSelectedUserId] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const data = await getUsers();
        setUsers(data);
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    const fetchFriendRequests = async () => {
      try {
        const data = await getFriendRequests();
        // Filter requests to show only pending ones
        const pendingRequests = data.filter((request) => request.estado === 'pendiente');
        setFriendRequests(pendingRequests);
      } catch (error) {
        console.error('Error fetching friend requests:', error);
      }
    };

    if (open) {
      fetchUsers();
      fetchFriendRequests();
    }
  }, [open]);

  const handleSendFriendRequest = async () => {
    if (selectedUserId) {
      try {
        const requestData = {
          remitente_id: currentUserId,
          destinatario_id: selectedUserId,
          estado: 'pendiente'
        };
        console.log('Request Data:', requestData);
        await createFriendRequest(requestData);
        alert('Friend request sent successfully');
        onClose();
      } catch (error) {
        console.error('Failed to send friend request:', error);
        alert('Failed to send friend request');
      }
    }
  };

  const handleAcceptFriendRequest = async (request) => {
    try {
      await updateFriendRequest(request.id, 'aceptado');
      setFriendRequests(friendRequests.filter((r) => r.id !== request.id));
      alert('Friend request accepted');
    } catch (error) {
      console.error('Failed to accept friend request:', error);
      alert('Failed to accept friend request');
    }
  };

  const handleDeclineFriendRequest = async (request) => {
    try {
      await updateFriendRequest(request.id, 'rechazado');
      setFriendRequests(friendRequests.filter((r) => r.id !== request.id));
      alert('Friend request declined');
    } catch (error) {
      console.error('Failed to decline friend request:', error);
      alert('Failed to decline friend request');
    }
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Friend Requests</DialogTitle>
      <DialogContent>
        <Typography variant="h6">Send Friend Request</Typography>
        <List>
          {users.map((user) => (
            <ListItem
              button
              key={user.id}
              selected={selectedUserId === user.id}
              onClick={() => setSelectedUserId(user.id)}
            >
              <ListItemAvatar>
                <Avatar src={user.foto_perfil} />
              </ListItemAvatar>
              <ListItemText primary={user.nombre} />
            </ListItem>
          ))}
        </List>
        <Typography variant="h6" style={{ marginTop: '20px' }}>Pending Friend Requests</Typography>
        <List>
          {friendRequests.map((request) => (
            <ListItem key={request.id}>
              <ListItemAvatar>
                <Avatar src={request.foto_perfil} />
              </ListItemAvatar>
              <ListItemText primary={request.nombre} />
              <Button variant="contained" color="primary" onClick={() => handleAcceptFriendRequest(request)}>
                Accept
              </Button>
              <Button variant="outlined" color="secondary" onClick={() => handleDeclineFriendRequest(request)}>
                Decline
              </Button>
            </ListItem>
          ))}
        </List>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="secondary">Cancel</Button>
        <Button onClick={handleSendFriendRequest} color="primary">Send Request</Button>
      </DialogActions>
    </Dialog>
  );
}

export default FriendRequestDialog;

