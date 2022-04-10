var Token = artifacts.require("Token");

module.exports = function (deployer) {
    deployer.deploy(Token, "BLACKFISH LABS", "BKF", 1000);
};