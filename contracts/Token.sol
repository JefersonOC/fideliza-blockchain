// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Token {
    string public name; //Name for the Crypto Token.
    string public symbol; //Symbol for the Crypto Token.
    address owner;
    mapping(address => uint256) public balance;
    uint256 public totalSupply;

    //Brand create their tokens when deploy this contract:
    //[BLACKFISH - BKF] 
    //Constructors are run only once, when the contract is initially deployed.
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply
    ) {
        owner = msg.sender;
        balance[msg.sender] = _initialSupply;
        totalSupply = _initialSupply;
        name = _name;
        symbol = _symbol;
    }

    //Transfer or gift Tokens to another account
    function transferTokens(address _account, uint256 _amount) public {
        require(balance[msg.sender] >= _amount, "Not enough funds");
        balance[msg.sender] -= _amount;
        balance[_account] += _amount;
    }

    //Mint new Tokens (Only owner can mint Tokens)
    function mint(uint256 _amount) public {
        require(owner == msg.sender, "Only owner can mint Tokens"); //Only owner can mint Tokens.
        totalSupply += _amount;
        balance[owner] += _amount;
    }

    //Redeem the tokens - Transfers Tokens to the main account/owner
    //You can show the transaction hash and redeem the tokens for gifts/goods.
    function redeemTokens(uint256 _amount) public {
        require(balance[msg.sender] >= _amount, "Not enough funds");
        balance[msg.sender] -= _amount;
        balance[owner] += _amount;
    }
}
