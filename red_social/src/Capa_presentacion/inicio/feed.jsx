import React, { useState, useEffect } from 'react';
import { Container, Box, Typography, Avatar, Card, CardHeader, CardContent, CardActions, IconButton, Button, List, ListItem, ListItemAvatar, ListItemText, Dialog, DialogTitle, DialogContent, DialogActions, TextField } from '@mui/material';
import { Favorite, Comment, Share } from '@mui/icons-material';
import { getPosts, getUsers } from '../../Capa_Datos/authService.js'; // Usar getUsers
import ChatComponent from './chat.jsx';
import Post from './post.jsx';
import './feed.css';

function Feed({ userId }) {
  const [selectedChatUser, setSelectedChatUser] = useState(null);
  const [friendRequests, setFriendRequests] = useState([]);
  const [friendRequestDialogOpen, setFriendRequestDialogOpen] = useState(false);
  const [posts, setPosts] = useState([]);
  const [friends, setFriends] = useState([]);
  const [loading, setLoading] = useState(true);
  const [postDialogOpen, setPostDialogOpen] = useState(false);

  useEffect(() => {
    const fetchFriends = async () => {
      try {
        const data = await getUsers(); // Usar getUsers en lugar de getFriends
        console.log('Friends fetched:', data);
        setFriends(data);
      } catch (error) {
        console.error('Error fetching friends:', error);
      } finally {
        setLoading(false);
      }
    };

    const fetchPosts = async () => {
      try {
        const data = await getPosts();
        console.log('Fetched posts:', data);
        const sortedData = data.sort((a, b) => new Date(b.fecha_publicacion) - new Date(a.fecha_publicacion));
        setPosts(sortedData);
      } catch (error) {
        console.error('Error fetching posts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchPosts();
    fetchFriends();
  }, []);

  const handleChatOpen = (user) => {
    setSelectedChatUser(user);
  };

  const handleChatClose = () => {
    setSelectedChatUser(null);
  };

  const handleFriendRequestDialogClose = () => {
    setFriendRequestDialogOpen(false);
  };

  const handleAcceptFriendRequest = (user) => {
    setFriendRequests(friendRequests.filter((request) => request.id !== user.id));
  };

  const handleDeclineFriendRequest = (user) => {
    setFriendRequests(friendRequests.filter((request) => request.id !== user.id));
  };

  const handleCreatePost = async (newPost) => {
    try {
      const completePost = {
        ...newPost,
        usuario_id: newPost.usuario_id || userId,
        fecha_publicacion: newPost.fecha_publicacion || new Date().toISOString(),
      };
      setPosts((prevPosts) => [completePost, ...prevPosts]);
    } catch (error) {
      console.error('Failed to create post:', error);
    }
  };

  if (loading) {
    return (
      <Container component="main" maxWidth="md" sx={{ mt: 8, display: 'flex' }}>
        <Typography variant="h6">Loading...</Typography>
      </Container>
    );
  }

  return (
    <Container component="main" maxWidth="md" sx={{ mt: 8, display: 'flex', backgroundColor: '#f0f0f0', borderRadius: '8px', padding: '16px' }}>
      <Box sx={{ flexGrow: 1 }}>
        <Button variant="contained" color="primary" onClick={() => setPostDialogOpen(true)}>
          Create Post
        </Button>
        <Box className="feed-box" sx={{ mt: 3 }}>
          {posts.length > 0 ? (
            posts.map((post) => (
              <Card key={post.id} className="feed-card" sx={{ mb: 3 }}>
                <CardHeader
                  avatar={<Avatar src={`https://via.placeholder.com/40?text=User${post.usuario_id}`} />}
                  title={`User ${post.usuario_id}`}
                  subheader={new Date(post.fecha_publicacion).toLocaleString()}
                />
                <CardContent>
                  <Typography variant="body1">{post.contenido}</Typography>
                </CardContent>
                <CardActions disableSpacing>
                  <IconButton aria-label="add to favorites">
                    <Favorite />
                    <Typography variant="body2" sx={{ ml: 1 }}>
                      {post.likes || 0}
                    </Typography>
                  </IconButton>
                  <IconButton aria-label="comment">
                    <Comment />
                    <Typography variant="body2" sx={{ ml: 1 }}>
                      {post.comments || 0}
                    </Typography>
                  </IconButton>
                  <IconButton aria-label="share">
                    <Share />
                  </IconButton>
                </CardActions>
                <Box className="comment-box" sx={{ p: 2 }}>
                  <TextField
                    variant="outlined"
                    fullWidth
                    placeholder="Add a comment..."
                  />
                  <Button variant="contained" color="primary" sx={{ mt: 1 }}>
                    Post
                  </Button>
                </Box>
              </Card>
            ))
          ) : (
            <Typography variant="body1">No posts available</Typography>
          )}
        </Box>
      </Box>
      <Box sx={{ width: 250, ml: 2, borderLeft: '1px solid #ddd', height: 'calc(100vh - 64px)', position: 'fixed', top: 64, right: 0, overflowY: 'auto' }}>
        <Typography variant="h6" sx={{ textAlign: 'center', mt: 2 }}>Friends</Typography>
        <List>
          {friends.map((user) => (
            <ListItem button key={user.id} onClick={() => handleChatOpen(user)}>
              <ListItemAvatar>
                <Avatar src={user.foto_perfil} />
              </ListItemAvatar>
              <ListItemText primary={user.nombre} />
            </ListItem>
          ))}
        </List>
      </Box>
      <Dialog open={friendRequestDialogOpen} onClose={handleFriendRequestDialogClose}>
        <DialogTitle>Friend Requests</DialogTitle>
        <DialogContent>
          <List>
            {friendRequests.map((user) => (
              <ListItem key={user.id}>
                <ListItemAvatar>
                  <Avatar src={user.avatar} />
                </ListItemAvatar>
                <ListItemText primary={user.username} />
                <Button variant="contained" color="primary" onClick={() => handleAcceptFriendRequest(user)}>
                  Accept
                </Button>
                <Button variant="outlined" color="secondary" onClick={() => handleDeclineFriendRequest(user)}>
                  Decline
                </Button>
              </ListItem>
            ))}
          </List>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleFriendRequestDialogClose} color="primary">
            Close
          </Button>
        </DialogActions>
      </Dialog>
      {selectedChatUser && (
        <ChatComponent user={selectedChatUser} onClose={handleChatClose} currentUserId={userId} />
      )}
      <Post open={postDialogOpen} onClose={() => setPostDialogOpen(false)} onCreatePost={handleCreatePost} userId={userId} />
    </Container>
  );
}

export default Feed;
