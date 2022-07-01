pragma solidity ^0.8.0;

contract Deployed {
    uint public a;

    event Log(string message);

    constructor (uint _a) public {
        a = _a;
    }

    function setA(uint _a) public {
        a = _a;
        emit Log("set a");
    }

    function getA() public returns (uint) {
        emit Log("get a");
        return a;
    }

}
//0x5caf109Ec2801c3b3e5fcD814fB1C2371F2A66d8