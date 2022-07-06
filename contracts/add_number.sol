pragma solidity ^0.8.0;

contract Number {
    uint public number;


    constructor (uint _a) public {
        number = _a;
    }

    function set(uint _a) public {
        number += _a;
    }

    function get() public view returns (uint) {
        return number;
    }

}
