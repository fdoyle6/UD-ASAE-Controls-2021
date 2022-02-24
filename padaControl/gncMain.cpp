#include "padaGNC.hpp"

int main(void) {

  State state;
  state.runInits();

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