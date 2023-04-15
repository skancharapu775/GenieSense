import React from 'react';
import '../App.css';
import Header from './Header.js';
import axios from 'axios';

class Image_to_Text extends React.Component {

    state = {
        selectedFile: null
    }

    fileSelectedHandler = (event) => {
        this.setState({
            selectedFile: event.target.files[0]
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
    }

    render () {
    return (
        <>
            <Header />
            <img className="divider" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Grey_background.jpg/1200px-Grey_background.jpg"></img>
            <p></p>
            <p>Here you can upload an image of your choice, and an audio file describing that image will be returned</p>
            <form>
                <input type="file" onChange={this.fileSelectedHandler} />
                <button type="button" onClick={this.fileUploadHandler}>Upload</button>
            </form>
        </>
    )
    }
}

export default Image_to_Text;