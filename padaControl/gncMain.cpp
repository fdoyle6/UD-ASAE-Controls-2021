#include <iostream>
#include "Eigen/Dense"
#include "startup.hpp"
#include ""

int main(void) {

  // Startup
  runInits();
  getColor();
  
  // Pre-release loop
  while (hasReleased == false){
    pollSensors();
    updateState();
    // check if released
  }

  // Target Acquisition
  
  // Descent Loop

  // Flare & Land Loop

  // Shutdown

  return 0;
}