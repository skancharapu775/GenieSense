import React from 'react';
import '../App.css';
import Header from './Header.js';
import axios from 'axios';
import RenderAudio from './renderaudio.js';
import { Input } from '@mui/material';
import { Button } from '@mui/material';

class Image_to_Text extends React.Component {

    state = {
        selectedFile: null,
        renderaudio: false,
    }

    fileSelectedHandler = (event) => {
        this.setState({
            selectedFile: event.target.files[0],
            renderaudio: false,
            url: '',
            hidden: true
        })
        this.setState({
            url: URL.createObjectURL(event.target.files[0])
          })

    }

    fileUploadHandler = () => {
        console.log(this.state.selectedFile)

        let file = this.state.selectedFile
        let formdata = new FormData()
        formdata.append('file', file)

        axios({
            method: 'post',
            url: 'http://localhost:5000/upload',
            data: formdata,
            headers: {'Content-Type': 'multipart/form-data'}
        }).then((res)=>{
            console.log(res)
        })
        this.setState({
            renderaudio: true
          })
    }

    render () {
    return (
        <>
            <Header />
            <img className="divider" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Grey_background.jpg/1200px-Grey_background.jpg"></img>
            <p></p>
            <p>Here you can upload an image of your choice, and an audio file describing that image will be returned</p>
            <form>
                <Button
                    variant="contained"
                    component="label"
                    >
                    Select File
                    <input hidden type="file" onChange={this.fileSelectedHandler} />
                </Button>
                <Button type="button" onClick={this.fileUploadHandler}>Upload</Button>
                </form>
                <img height="300" src={this.state.url}/>
                <h1></h1>
                <RenderAudio renderaudio={this.state.renderaudio} />
                
        </>
    )
    }
}

export default Image_to_Text;