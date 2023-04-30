import React, { useState } from 'react';
import {InputGroup, FormControl, Button} from 'react-bootstrap';

function SearchBar() {
  const [searchText, setSearchText] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    console.log(`Searching for ${searchText}`);
  };

  return (
    <div className="d-flex justify-content-center mt-5">
      <InputGroup>
        <FormControl
          type="text"
          placeholder="Search"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
        />
        <Button variant="outline-secondary" onClick={handleSearch}>
          <i className="bi bi-search"></i>
        </Button>
      </InputGroup>
    </div>
  );
}

export default SearchBar;
