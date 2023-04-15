import * as React from "react";
// importing material UI components
import { AppBar, Toolbar, IconButton, Typography, Stack, Button } from '@mui/material';
import Box from '@mui/material/Box';
import '../App.css';
  
export default function Header() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static"  style={{ background: 'transparent', boxShadow: 'none'}}>
        <Toolbar>
          {/* The Typography component applies D
           default font weights and sizes */}
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='80' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096868873816514590/image.png" alt="logo" height='35' />
          <img src="https://cdn.discordapp.com/attachments/915276863272800297/1096855750330044466/geniesense.png" alt="logo" height='100' />
        </Toolbar>
        <h1>Image to Audio</h1>
      </AppBar>
      </Box>
  );
}