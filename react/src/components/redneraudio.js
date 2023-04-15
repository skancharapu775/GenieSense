import React from 'react'
import {Typography} from '@mui/material';
import '../App.css'

export default function FlashcardList({ renderaudio }) {
  console.log('renderaudio: ', renderaudio)
  if (!renderaudio) {
    return null;
  }
  return (
    <div>
      <audio
          controls
          src="http://localhost:5000/audiofile"
          >
          Your browser does not support the
          <code>audio</code> element.
      </audio>
    </div>
  )
}
