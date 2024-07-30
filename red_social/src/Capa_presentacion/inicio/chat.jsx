import React, { useState, useEffect, useRef } from 'react';
import { Box, Typography, TextField, Button, List, ListItem, ListItemText, Paper, IconButton } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { getMessagesBySenderAndRecipient, createMessage, deleteMessage } from '../../Capa_Datos/authService';
import "../../styles/chat.css";

const Chat = ({ user, onClose, currentUserId }) => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const messagesEndRef = useRef(null);

  // Función para cargar los mensajes
  const fetchMessages = async () => {
    if (!user || !user.id) return;
    try {
      const responseArray = await getMessagesBySenderAndRecipient(currentUserId, user.id);
      console.log('Mensajes cargados:', responseArray);

      const response = responseArray[0];
      const { data } = response;
      if (data && Array.isArray(data)) {
        setMessages(data);
      } else {
        console.error('La respuesta no contiene un array de mensajes');
      }
      scrollToBottom();
    } catch (error) {
      console.error('Error fetching messages:', error);
    }
  };

  // Ejecutar la función fetchMessages cuando se abre el chat
  useEffect(() => {
    if (user && user.id) {
      fetchMessages();
      const interval = setInterval(() => {
        fetchMessages();
      }, 5000);

      return () => clearInterval(interval);
    }
  }, [user]);

  // Función para desplazar la vista al final
  const scrollToBottom = () => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleSendMessage = async () => {
    if (newMessage.trim() === '') return;
    if (!user || !user.id) return;

    const messageData = {
      remitente_id: currentUserId,
      destinatario_id: user.id,
      contenido: newMessage,
    };

    try {
      await createMessage(messageData);
      console.log('Mensaje enviado');
      setNewMessage('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  const handleDeleteMessage = async (messageId) => {
    try {
      await deleteMessage(messageId);
      setMessages((prevMessages) => prevMessages.filter((msg) => msg.id !== messageId));
    } catch (error) {
      console.error('Error deleting message:', error);
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    if (isNaN(date)) {
      return 'Invalid Date';
    }
    return date.toLocaleString();
  };

  if (!user || !user.id) {
    return null;
  }

  return (
    <Paper sx={{ position: 'fixed', bottom: 0, right: 0, width: 300, height: 400, bgcolor: '#fff', borderRadius: 2, boxShadow: 3 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', p: 1, bgcolor: '#f5f5f5', borderTopLeftRadius: 2, borderTopRightRadius: 2 }}>
        <Typography variant="subtitle1">
          Chat with {user.nombre}
        </Typography>
        <IconButton size="small" onClick={onClose}>
          <CloseIcon />
        </IconButton>
      </Box>
      <Box sx={{ height: 'calc(100% - 120px)', overflowY: 'auto', p: 2 }}>
        <List>
          {messages.map((message) => (
            <ListItem 
              key={message.id} 
              className={message.remitente_id === currentUserId ? 'sentMessage' : 'receivedMessage'}
              sx={{ 
                display: 'flex', 
                justifyContent: message.remitente_id === currentUserId ? 'flex-end' : 'flex-start' 
              }}
            >
              <ListItemText primary={message.contenido} secondary={formatDate(message.fecha_envio)} />
              {message.remitente_id === currentUserId && (
                <Button variant="outlined" color="secondary" size="small" onClick={() => handleDeleteMessage(message.id)}>
                  Delete
                </Button>
              )}
            </ListItem>
          ))}
          <div ref={messagesEndRef} />
        </List>
      </Box>
      <Box sx={{ display: 'flex', alignItems: 'center', p: 1, borderTop: '1px solid #ddd' }}>
        <TextField
          fullWidth
          variant="outlined"
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
          placeholder="Type a message"
          size="small"
        />
        <Button variant="contained" color="primary" onClick={handleSendMessage} sx={{ ml: 1 }}>
          Send
        </Button>
      </Box>
    </Paper>
  );
};

export default Chat;

