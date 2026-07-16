-- Generate default admin user
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
  "36c9050e-ddd3-4c3b-9731-9f487208bbc1",
  "Admin",
  "HBnB",
  "admin@hbnb.io",
  "$2a$12$6uE7BlLvWAYmlmZbCPnlRue4sC4dFhJnOlo7PuZLc2DCHrXdCsuj2", -- admin1234 hashed using bcrypt2
  true
);

-- Generate default amenities
INSERT INTO amenities (id, name)
VALUES 
  ("1f5856a3-d923-4df7-a6b8-419ddd8c33ef", "WiFi"),
  ("a00dc875-bc71-48ef-a7c3-341e0e851452", "Swimming Pool"),
  ("657b3e15-6f42-4d9b-a060-781567c0032b", "Air Conditioning");
