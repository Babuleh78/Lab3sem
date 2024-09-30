   Feature: Square color
     Scenario: Create a red square
       Given I have a red color
       When I create a square with that color
       Then it should return "Квадрат, цвет: красный"

   