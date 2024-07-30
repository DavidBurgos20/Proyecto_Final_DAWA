import React, { useState, useEffect } from 'react';
import {
  AppBar, Toolbar, Typography, Box, InputBase, IconButton, Badge, Menu, MenuItem,
  List, ListItem, ListItemAvatar, Avatar, Button, ListItemText
} from '@mui/material';
import { Search, AccountCircle, People, Add } from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';
import './Navbar.css';
import { getUsers, getFriendRequests, createFriendRequest, deleteFriendRequest, updateFriendRequest } from '../../Capa_Datos/authService';
import FriendRequestDialog from './FriendRequestDialog.jsx';

function Navbar({ onCreatePost, onLogout, currentUserId }) {
  const navigate = useNavigate();
  const [anchorEl, setAnchorEl] = useState(null);
  const [searchResults, setSearchResults] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [friendRequests, setFriendRequests] = useState([]);
  const [friendRequestDialogOpen, setFriendRequestDialogOpen] = useState(false);
  const [users, setUsers] = useState([]);

  useEffect(() => {
    console.log("Current User ID in Navbar:", currentUserId);
    const fetchFriendRequests = async () => {
      try {
        const data = await getFriendRequests();
        setFriendRequests(data);
      } catch (error) {
        console.error('Failed to fetch friend requests:', error);
      }
    };

    const fetchUsers = async () => {
      try {
        const data = await getUsers();
        setUsers(data);
      } catch (error) {
        console.error('Failed to fetch users:', error);
      }
    };

    fetchFriendRequests();
    fetchUsers();
  }, [currentUserId]);

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
    if (event.target.value.trim() === '') {
      setSearchResults([]);
    } else {
      setSearchResults(
        users.filter((user) =>
          user.username.toLowerCase().includes(event.target.value.toLowerCase())
        )
      );
    }
  };

  const handleSendFriendRequest = async (user) => {
    try {
      const requestData = {
        remitente_id: currentUserId,
        destinatario_id: user.id,
        estado: 'pendiente'
      };
      console.log('Request Data:', requestData);
      await createFriendRequest(requestData);
      alert(`Friend request sent to ${user.username}`);
    } catch (error) {
      console.error('Failed to send friend request:', error);
      alert('Failed to send friend request.');
    }
  };

  const handleFriendRequestDialogOpen = () => {
    setFriendRequestDialogOpen(true);
  };

  const handleFriendRequestDialogClose = () => {
    setFriendRequestDialogOpen(false);
  };

  const handleAcceptFriendRequest = async (user) => {
    try {
      await updateFriendRequest(user.id, { estado: 'aceptado' });
      setFriendRequests(friendRequests.filter((request) => request.id !== user.id));
    } catch (error) {
      console.error('Failed to accept friend request:', error);
      alert('Failed to accept friend request.');
    }
  };

  const handleDeclineFriendRequest = async (user) => {
    try {
      await deleteFriendRequest(user.id);
      setFriendRequests(friendRequests.filter((request) => request.id !== user.id));
    } catch (error) {
      console.error('Failed to decline friend request:', error);
      alert('Failed to decline friend request.');
    }
  };

  const handleLogoClick = () => {
    navigate('/feed');
  };

  const handleProfileClick = () => {
    navigate('/profile');
    handleMenuClose();
  };

  const handleLogout = () => {
    onLogout();
    navigate('/');
    handleMenuClose();
  };

  const menuId = 'primary-search-account-menu';

  return (
    <AppBar position="fixed">
      <Toolbar>
        <Typography variant="h6" noWrap component="div" onClick={handleLogoClick} style={{ cursor: 'pointer' }}>
          SocialU
        </Typography>
        <Box sx={{ flexGrow: 1 }} />
        <Box sx={{ position: 'relative', borderRadius: 1, backgroundColor: 'rgba(255, 255, 255, 0.15)', '&:hover': { backgroundColor: 'rgba(255, 255, 255, 0.25)' }, marginLeft: 2, width: 'auto' }}>
          <Box sx={{ padding: '0 16px', height: '100%', position: 'absolute', pointerEvents: 'none', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Search />
          </Box>
          <InputBase
            placeholder="Search…"
            sx={{ color: 'inherit', paddingLeft: `calc(1em + 32px)`, width: '100%' }}
            value={searchQuery}
            onChange={handleSearchChange}
          />
          {searchResults.length > 0 && (
            <Box sx={{ position: 'absolute', top: '100%', left: 0, width: '100%', backgroundColor: '#fff', boxShadow: 3, zIndex: 1500 }}>
              <List>
                {searchResults.map((user) => (
                  <ListItem key={user.id} button>
                    <ListItemAvatar>
                      <Avatar src={user.avatar} />
                    </ListItemAvatar>
                    <ListItemText primary={user.username} />
                    <Button variant="contained" color="primary" onClick={() => handleSendFriendRequest(user)}>
                      Send Friend Request
                    </Button>
                  </ListItem>
                ))}
              </List>
            </Box>
          )}
        </Box>
        <Box sx={{ flexGrow: 1 }} />
        <Box>
          <IconButton color="inherit" onClick={handleFriendRequestDialogOpen}>
            <Badge badgeContent={friendRequests.length} color="error">
              <People />
            </Badge>
          </IconButton>
          <IconButton color="inherit" onClick={onCreatePost}>
            <Add />
          </IconButton>
          <IconButton edge="end" aria-label="account of current user" aria-controls={menuId} aria-haspopup="true" onClick={handleProfileMenuOpen} color="inherit">
            <AccountCircle />
            <Typography variant="body1" sx={{ marginLeft: 1 }}>
              {currentUserId}
            </Typography>
          </IconButton>
        </Box>
      </Toolbar>
      <Menu
        anchorEl={anchorEl}
        anchorOrigin={{ vertical: 'top', horizontal: 'right' }}
        id={menuId}
        keepMounted
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        open={Boolean(anchorEl)}
        onClose={handleMenuClose}
      >
        <MenuItem onClick={handleProfileClick}>Profile</MenuItem>
        <MenuItem onClick={handleLogout}>Logout</MenuItem>
      </Menu>
      <FriendRequestDialog
        open={friendRequestDialogOpen}
        onClose={handleFriendRequestDialogClose}
        currentUserId={currentUserId}
        friendRequests={friendRequests}
        handleAcceptFriendRequest={handleAcceptFriendRequest}
        handleDeclineFriendRequest={handleDeclineFriendRequest}
      />
    </AppBar>
  );
}

export default Navbar;

