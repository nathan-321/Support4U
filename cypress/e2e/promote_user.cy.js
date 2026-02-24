describe("Promote User", { testIsolation: false }, () => {
  before(() => {
    cy.admin_login();
  });

  it("promotes regular user", () => {
    cy.get('[data-testid="promote_user_button"]').click();
    cy.contains("td", "Emily").closest("tr").find("button").click();
    cy.contains(`Emily is now admin!`).should("be.visible");
  });

  it("demotes admin", () => {
    cy.get('[data-testid="promote_user_button"]').click();
    cy.contains("td", "Emily").closest("tr").find("button").click();
    cy.contains(`Emily has been demoted to a regular user!`).should(
      "be.visible"
    );
  });
});
