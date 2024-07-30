import React, { useState } from 'react';
import { Button, TextField, Dialog, DialogTitle, DialogContent, DialogActions } from '@mui/material';
import { createPost } from '../../Capa_Datos/authService'; // Importar la función de crear post

function Post({ open, onClose, onCreatePost, userId }) {
  const [content, setContent] = useState('');

  const handleCreatePost = async () => {
    if (content.trim() !== '') {
      try {
        const newPost = await createPost(userId, content); // Utilizamos el ID del usuario pasado como prop
        onCreatePost(newPost);
        setContent('');
        onClose();
      } catch (error) {
        console.error('Failed to create post:', error);
      }
    }
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>Create a New Post</DialogTitle>
      <DialogContent>
        <TextField
          autoFocus
          margin="dense"
          label="Post Content"
          type="text"
          fullWidth
          multiline
          rows={4}
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="secondary">Cancel</Button>
        <Button onClick={handleCreatePost} color="primary">Post</Button>
      </DialogActions>
    </Dialog>
  );
}

export default Post;

