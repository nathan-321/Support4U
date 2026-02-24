describe("Promote User", { testIsolation: false }, () => {
  before(() => {
    cy.admin_login();
  });

  it("adds new ticket and displays on dashboard", () => {
    cy.get('[data-testid="new_ticket_button"]').click();
    cy.get('[data-testid="ticket_title"]').type("Require new laptop");
    cy.get('[data-testid="ticket_description"]').type(
      "My laptop is breaking and I would like to request a new laptop"
    );
    cy.get('[data-testid="ticket_priority"]').type("4");
    cy.get('[data-testid="ticket_status"]').select("In Progress");
    cy.get('[data-testid="new_ticket_submit"]').click();
    cy.contains("td", "Require new laptop")
      .parent()
      .should("contain", "Nathan")
      .should("contain", "4")
      .should("contain", "In Progress");
  });

  it("modify ticket", () => {
    cy.contains("td", "Require new laptop")
      .closest("tr")
      .find('[data-testid="edit_ticket_button"]')
      .click();
    cy.wait(1000);
    cy.get('[data-testid="ticket_priority"]').clear().type("5");
    cy.get('[data-testid="update_ticket_submit"]').click();
    cy.contains("td", "Require new laptop").parent().should("contain", "5");
    cy.contains(`Ticket updated successfully!`).should("be.visible");
  });

  it("deletes ticket", () => {
    cy.contains("td", "Require new laptop")
      .closest("tr")
      .find('[data-testid="delete_ticket_button"]')
      .click();
    cy.contains(`Ticket deleted successfully!`).should("be.visible");
  });
});
