var Token = artifacts.require("Token");

module.exports = function (deployer) {
    deployer.deploy(Token, "BLACKFISH LABS", "BKF", 1000, { from: '0xc81985962e853ae5408d7C4dEd69BF3459FaA96C' });
};