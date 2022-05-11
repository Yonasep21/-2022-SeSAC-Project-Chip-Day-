import React, { useEffect, useState } from "react";
import SearchHeader from "./components/search_header/search_header";
import VideoList from "./components/video_list/video_list";
import styles from "./app.module.css";

function App() {
  const [videos, setVideos] = useState([]);

  const search = query => {
    // console.log(query)

    const requestOptions={
      method: 'GET',
      redirect: 'follow'
    };

    fetch(`/contents/title/${query}`, requestOptions)
      .then(response => response.json())
      .then(result => setVideos(result.Data))
      .catch(error => console.log('error', error));
  }

  useEffect(() => {
    const requestOptions = {
      method: "GET",
      redirect: "follow",
    };

    fetch("all", requestOptions)
      .then(response => response.json())
      .then((result) => console.log(result.Data))
      // .then((data) => console.log(data))
      .catch((error) => console.log("error", error));
  }, []);

  return (
    <div className={styles.app}>
      <SearchHeader onSearch={search} />
      <VideoList videos={videos}/>
      {/* <h1>hi</h1> */}
    </div>
  );
}
export default App;
