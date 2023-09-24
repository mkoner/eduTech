import React, { useState } from 'react';
import styled, { createGlobalStyle } from 'styled-components';

const theme = {
    primary: '#007bff', // a shade of blue
    secondary: '#6c757d', // a shade of gray
    light: '#f8f9fa',
    dark: '#343a40',
    font: 'Roboto, sans-serif',
    cardBackground: '#F5F5DC', // a beige color
    footerBackground: '#8B4513',
};

const GlobalStyle = createGlobalStyle`
    body {
        font-family: ${theme.font};
        margin: 0;
    }
`;

const HomepageContainer = styled.div`
    text-align: center;
`;

const Header = styled.header`
    background: linear-gradient(to right, ${theme.primary}, ${theme.secondary});
    color: white;
    padding: 20px 0;
    position: relative;
`;

const SearchContainer = styled.div`
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
`;

const SearchForm = styled.form`
    display: flex;
`;

const SearchBar = styled.input.attrs({ type: 'search' })`
    padding: 5px;
    border-radius: 5px;
    border: none;
`;

const SearchButton = styled.button`
    padding: 5px 10px;
    border-radius: 5px;
    border: none;
    background-color: ${theme.primary};
    color: white;
`;

const Hero = styled.section`
    background-image: url('https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/hands-of-african-children-need-help-uygargeographic.jpg');
    height: 300px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
`;

const CardContainer = styled.section`
    display: flex;
    justify-content: space-around;
`;

const Card = styled.div`
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px auto;
    width: 40%;
    height: 500px;
    border-radius: 15px;
    background-color: ${theme.cardBackground};  

    &:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transform: scale(1.05);
        transition: all 0.3s ease-in-out;
    }
`;
const Button = styled.button`
    padding: 0.5em 1em;
    margin-right: 0.5em;
`;


const Footer = styled.footer`
    background-color: ${theme.footerBackground};
   color: ${theme.light}; // assuming you want a light text color that contrasts with the dark background
   padding: 20px 0;
`;

const Homepage = () => {
    const [searchTerm, setSearchTerm] = useState('');

    const handleSearchChange = (event) => {
	setSearchTerm(event.target.value);
    };

    const handleSearchSubmit = (event) => {
	event.preventDefault();
	// Handle search submit...
    };

    return (
	<>
	    <GlobalStyle />
	    <HomepageContainer>
		<Header>
		    <h1>Welcome to EduTech</h1>
		    <p>Empowering African Students Through Technology</p>
		    <SearchContainer>
			<SearchForm onSubmit={handleSearchSubmit}>
			    <SearchBar value={searchTerm} onChange={handleSearchChange} placeholder="Search..." />
			    <SearchButton type="submit">Go</SearchButton>
			</SearchForm>
		    </SearchContainer>
		</Header>
		<Hero />
		<CardContainer>
		    <Card>
			<h2>About Us</h2>
			<p>EduTech is an e-learning platform dedicated to helping African students learn tech. We offer a wide range of courses in various tech fields.</p>
		    </Card>
		    <Card>
			<h2>Our Courses</h2>
			<p>Explore our extensive course library and start learning today!</p>
			<Button>View Courses</Button>
		    </Card>
		</CardContainer>
		<Footer>
		    <p>© 2023 EduTech. All rights reserved.</p>
		</Footer>
	    </HomepageContainer>
	</>
    );
};

export default Homepage;

