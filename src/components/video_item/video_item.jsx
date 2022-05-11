import React from "react";
import styles from './video_item.module.css'

// const VideoItem = ({video}) => (
//   <li className={styles.video}>
//     <img className={styles.thumnail} src={video.POSTER} alt="poster" />
//     <div>
//         <p className={styles.title}>{video.TITLE_KR}</p>
//         <p className={styles.channel}>{video.GENRE}</p>
//     </div>
//   </li>
// );

// export default VideoItem;

// import styles from './video_item.module.css'


const VideoItem = ({video}) => (
  // <li className={styles.container}>
  // <div className={styles.video}>
  //   <img className={styles.thumbnail} src={video.Poster} alt="poster" />
  //   <div className={styles.metadata}>
  //       <p className={styles.title}> {video.TitleKr} </p>
  //       <p className={styles.channel}> {video.Genre}</p>
  //       <p className={styles.channel}> {video.Imdb}</p>
  //       <p className={styles.channel}> {video.Year}</p>

  //       </div>
  //   </div>
  // </li>

   <li className={styles.container}>
  <div className={styles.video}>
    <img className={styles.thumbnail} src={video.Poster} alt="poster" />
    <div className={styles.metadata}>
        <p className={styles.title}> {video.TitleKr} </p>
        <p className={styles.channel}> {video.Genre}</p>
        <p className={styles.channel}> {video.Imdb}</p>
        <p className={styles.channel}> {video.Year}</p>

        </div>
    </div>
  </li>

);

export default VideoItem;
