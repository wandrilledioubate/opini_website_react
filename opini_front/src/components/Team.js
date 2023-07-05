import React from 'react';
import './Team.css';

const Team = ({ members }) => {
  return (
    <div className="team-container">
      <h1>Notre Équipe</h1>
      <div className="team-members">
        {members.map((member, index) => (
          <div className="member-card" key={index}>
            <img src={member.photo} alt={member.name} className="member-photo" />
            <h2 className="member-name">{member.name}</h2>
            <p className="member-description">{member.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Team;
