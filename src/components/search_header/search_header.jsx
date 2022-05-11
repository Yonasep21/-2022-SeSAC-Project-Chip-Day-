import React, { useRef } from 'react';
import styles from "./search_header.module.css"


const SearchHeader = ({onSearch}) => {
  const inputRef = useRef();
  const handleSearch =()=>{
    const value = inputRef.current.value;
    onSearch(value)
    // console.log(onSearch)
    //
  };
  

 const onClick = () => {
  handleSearch();
}

const onKeyPress= (event) =>{
  if(event.key === 'Enter'){
    handleSearch()
 }
};

  return(
      
      <header className={styles.hi}>
        <div className={styles.logo}>
        <img className={styles.img} src="/images/logo.png" alt="logo" />
        <h1 className={styles.title}>Chipday</h1>
        </div>
        <input className={styles.input} ref={inputRef}  type="search" placeholder="Search..." onKeyPress={onKeyPress}/>
        <button className={styles.button} type="submit" onClick={onClick}>
          <img className={styles.buttonImg} src="/images/search.png" alt="search" />
        </button>
      </header>
  )
      
};

export default SearchHeader;