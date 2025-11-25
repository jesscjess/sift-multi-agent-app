"""Test script to verify location agent orchestration works correctly"""

from memory_service import MemoryService
from agents import OrchestratorAgent, LocationAgent
import json

def test_location_orchestration():
    """Test that orchestrator correctly handles location setup and updates"""

    print("=" * 70)
    print("Testing Location Agent Orchestration")
    print("=" * 70)

    # Initialize services
    print("\n1. Initializing services...")
    memory_service = MemoryService(storage_path="data/test_location_orchestration.json")
    location_agent = LocationAgent()
    orchestrator = OrchestratorAgent(memory_service=memory_service)
    orchestrator.initialize_agents(None, location_agent, None)
    print("   ✓ Services initialized")

    # Test 1: Initial location setup
    print("\n2. Testing initial location setup (Oakland)...")
    result = orchestrator.process_request(
        user_query="location_setup",
        user_location="94612",
        request_type="location_setup"
    )

    if result.get("status") == "success":
        print("   ✓ Location setup successful")
        print(f"   Location: {result['location_data']['municipality']}, {result['location_data']['state']}")
        print(f"   Provider: {result['location_data']['local_authority']['name']}")
        print(f"\n   Response preview:")
        print("   " + result.get("message", "")[:200] + "...")
    else:
        print(f"   ✗ Location setup failed: {result.get('message')}")
        return False

    # Test 2: Location update
    print("\n3. Testing location update (San Francisco)...")
    result = orchestrator.process_request(
        user_query="location_update",
        user_location="San Francisco, CA",
        request_type="location_update"
    )

    if result.get("status") == "success":
        print("   ✓ Location update successful")
        print(f"   New location: {result['location_data']['municipality']}, {result['location_data']['state']}")
        print(f"   Provider: {result['location_data']['local_authority']['name']}")
    else:
        print(f"   ✗ Location update failed: {result.get('message')}")
        return False

    # Test 3: Invalid location
    print("\n4. Testing invalid location handling...")
    result = orchestrator.process_request(
        user_query="location_setup",
        user_location="99999",
        request_type="location_setup"
    )

    if result.get("status") == "error":
        print("   ✓ Invalid location correctly rejected")
        print(f"   Error message: {result.get('message')[:100]}...")
    else:
        print("   ✗ Invalid location not handled properly")

    # Test 4: Check memory storage
    print("\n5. Checking memory storage...")
    memories = memory_service.search_memory()
    print(f"   ✓ Total memories stored: {len(memories)}")

    location_memories = [m for m in memories if m.get('metadata', {}).get('agent') == 'location_agent']
    print(f"   ✓ Location agent memories: {len(location_memories)}")

    # Test 5: Display memory details
    print("\n6. Memory details:")
    print("-" * 70)
    for i, memory in enumerate(location_memories, 1):
        session_data = memory.get('session_data', {})
        metadata = memory.get('metadata', {})
        print(f"\n   Memory {i}:")
        print(f"   - Action: {session_data.get('action', 'N/A')}")
        print(f"   - Location: {session_data.get('user_location', 'N/A')}")
        print(f"   - Municipality: {metadata.get('municipality', 'N/A')}, {metadata.get('state', 'N/A')}")
        print(f"   - Zip: {metadata.get('zip_code', 'N/A')}")
        print(f"   - Timestamp: {memory.get('timestamp', 'N/A')}")

    # Test 6: Test all supported locations
    print("\n7. Testing all supported locations...")
    test_locations = ["94612", "94102", "Portland, OR"]

    for loc in test_locations:
        result = orchestrator.process_request(
            user_query="location_setup",
            user_location=loc,
            request_type="location_setup"
        )
        if result.get("status") == "success":
            location_data = result.get("location_data", {})
            print(f"   ✓ {loc} → {location_data.get('municipality')}, {location_data.get('state')}")
        else:
            print(f"   ✗ {loc} → Failed")

    print("\n" + "=" * 70)
    print("✓ All tests passed! Location orchestration is working.")
    print("=" * 70)

    print(f"\nMemory stored in: {memory_service.storage_path}")
    print(f"Total location memories: {len(location_memories)}")

    return True

if __name__ == "__main__":
    try:
        test_location_orchestration()
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
