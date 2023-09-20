import React, { useState } from 'react';
import styled, { createGlobalStyle } from 'styled-components';

// Use a custom theme to define colors and fonts
const theme = {
    primary: '#007bff',
    secondary: '#6c757d',
    light: '#f8f9fa',
    dark: '#343a40',
    font: 'Roboto, sans-serif'
};

// Use a global style to apply the theme to the body element
const GlobalStyle = createGlobalStyle`
    body {
        font-family: ${theme.font};
        margin: 0;
    }
`;

// Use a styled component for the homepage container
const HomepageContainer = styled.div`
    text-align: center;
`;

// Use a styled component for the header with a gradient background
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
    width: 200px;
`;

const SearchButton = styled.button`
    padding: 5px 10px;
    border-radius: 5px;
    border: none;
    background-color: ${theme.primary};
    color: white;
    width: 100px;
`;


// Use a styled component for the hero section with a background image
const Hero = styled.section`
    background-image: url('https://africanreporter.co.za/wp-content/uploads/sites/32/2015/09/children_silhouettes_holding_hands_up_by_macinivnw-d68n02c.jpg');
    height: 300px;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
`;
const CardContainer = styled.section`
    display: flex;
    justify-content: space-around;
`;

// Use a styled component for the section with a box shadow
const Card = styled.div`
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 20px auto;
    width: 30%;
    height: 200px;
    border: 2px solid ${theme.dark}; // Make the border bolder
    border-radius: 15px; // Make the border curved
     &:hover {
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transform: scale(1.05);
        transition: all 0.3s ease-in-out;
    }
`;
                           

// Use a styled component for the footer with a fixed position
const Footer = styled.footer`
    background-color: ${theme.light};
    color: ${theme.dark};
    padding: 20px 0;
    position: fixed;
    width: 100%;
    bottom: 0;
`;

// Use a styled component for the button with a hover effect
const Button = styled.button`
    background-color: ${theme.primary};
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    cursor: pointer;

    &:hover {
        background-color: ${theme.secondary};
        transform: scale(1.1);
        transition: all 0.3s ease-in-out;
    }
`;

// Use a functional component for the homepage
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
			    <SearchBar value={searchTerm} onChange={handleSearchChange}placeholder="Search..." />
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
