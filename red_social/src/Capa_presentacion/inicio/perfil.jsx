import React, { useEffect, useState } from 'react';
import { Container, Box, Typography, Avatar, Card, CardHeader, CardContent, CardActions, IconButton } from '@mui/material';
import { Favorite, Comment, Share } from '@mui/icons-material';
import { getUserDetails, getUserPosts } from '../../Capa_Datos/authService'; // Importar las funciones creadas
import './perfil.css';

function Perfil({ userId }) { // Asegúrate de recibir userId como prop
  const [userDetails, setUserDetails] = useState({});
  const [userPosts, setUserPosts] = useState([]);

  useEffect(() => {
    const fetchUserDetails = async () => {
      try {
        const data = await getUserDetails(userId);
        setUserDetails(data);
      } catch (error) {
        console.error('Error fetching user details:', error);
      }
    };

    const fetchUserPosts = async () => {
      try {
        const data = await getUserPosts(userId);
        setUserPosts(data);
      } catch (error) {
        console.error('Error fetching user posts:', error);
      }
    };

    fetchUserDetails();
    fetchUserPosts();
  }, [userId]);

  return (
    <Container component="main" maxWidth="md" className="profile-container">
      <Box className="profile-header">
        <Avatar src={userDetails.foto_perfil || 'https://via.placeholder.com/150'} className="profile-avatar" />
        <Box className="profile-details">
          <Typography className="profile-username">{userDetails.nombre}</Typography>
          <Typography className="profile-bio">{userDetails.biografia}</Typography>
          <Typography className="profile-joined">Joined on {new Date(userDetails.fecha_creacion).toLocaleDateString()}</Typography>
        </Box>
      </Box>
      <Typography variant="h5" sx={{ mb: 2 }}>Posts</Typography>
      <Box className="profile-posts">
        {userPosts.map((post) => (
          <Card key={post.id} className="feed-card" sx={{ mb: 3 }}>
            <CardHeader
              avatar={<Avatar src={`https://via.placeholder.com/40?text=User${post.usuario_id}`} />}
              title={userDetails.nombre}
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
          </Card>
        ))}
      </Box>
    </Container>
  );
}

export default Perfil;


