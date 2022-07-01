// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Wallet {
    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    receive() external payable {}

    function send(address _a, uint _amount) external {
        //require(msg.sender == owner, "caller is not owner");
        payable(_a).transfer(_amount);
    }// c.send('0.005 ether', '0x3f39Bc16ef847C0Cc74b751C4316109B7977c872', {'from': acct})

    function getBalance() external view returns (uint) {
        return address(this).balance;
    }

    function sendViaCall(address payable _to) public payable {
        // Call returns a boolean value indicating success or failure.
        // This is the current recommended method to use.
        (bool sent, bytes memory data) = _to.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
    }
}
//0x4D0b2fd0e4c586d3226d734D2Dc13A53Daf3a600
//0x67d06397AD91Aeb44b22C5291814C437Fb05059E
//0xfa46491dEC57C485b3c08889a3fab7050cC2c1d4
//0x63b32D50947e5CBEaF8a3676Bcae6e6bd36AF31C
//0x140F57431d4Ccc768dC22f04A419A103f7e50824