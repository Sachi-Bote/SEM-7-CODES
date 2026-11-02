
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    Student[] public students;

    function addStudent(uint _rollNo, string memory _name, uint _marks) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    function getStudent(uint index) public view returns (uint, string memory, uint) {
        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    fallback() external payable {}

    receive() external payable {}
}
