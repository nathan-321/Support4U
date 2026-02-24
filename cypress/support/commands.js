// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add("login", (username, password) => {
  cy.clearCookies();
  cy.clearLocalStorage();
  cy.visit("/");
  cy.get('[data-testid="login_form"]');
  cy.get('[data-testid="username_input"]').type(username);
  cy.get('[data-testid="password_input"]').type(password);
  cy.get('[data-testid="submit_button"]').click();
  cy.contains(`Login successful! Hello, ${username}`).should("be.visible");
});

Cypress.Commands.add("admin_login", () => {
  cy.login("Nathan", "nathan");
});

Cypress.Commands.add("user_login", () => {
  cy.login("Julie", "julie");
});
