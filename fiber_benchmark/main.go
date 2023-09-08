// main.go
package main

import (
	"fmt"
	"time"

	"github.com/gofiber/fiber/v2"
)

// Define a struct for user data
type UserModel struct {
	ID           int
	LastLogin    string
	IsSuperuser  bool
	Username     string
	FirstName    string
	LastName     string
	Email        string
	IsStaff      bool
	IsActive     bool
	DateJoined   string
}

// Define Fiber app
func setupFiberApp() *fiber.App {
	app := fiber.New()
	app.Get("/benchmark_user_model_serializer", BenchmarkUserModelSerializer)
	app.Get("/benchmark_user_read_only_model_serializer", BenchmarkUserReadOnlyModelSerializer)
	app.Get("/benchmark_user_serializer", BenchmarkUserSerializer)
	return app
}

// Define Fiber route handler for UserModelSerializer benchmark
func BenchmarkUserModelSerializer(c *fiber.Ctx) error {
	// Measure the time it takes to serialize using UserModel
	startTime := time.Now()
	for i := 0; i < 5000; i++ {
		_ = UserModel{
			ID:          1,
			LastLogin:   "2023-09-08T12:34:56",
			IsSuperuser: false,
			Username:    "hakib",
			FirstName:   "haki",
			LastName:    "benita",
			Email:       "me@hakibenita.com",
			IsStaff:     false,
			IsActive:    true,
			DateJoined:  "2023-09-08T12:34:56",
		}
	}
	endTime := time.Now()

	executionTimeMs := endTime.Sub(startTime).Milliseconds()

	return c.JSON(fiber.Map{
		"execution_time_ms": fmt.Sprintf("%d ms", executionTimeMs),
		"data":              createMockUser(),
	})
}

// Define Fiber route handler for UserReadOnlyModelSerializer benchmark
func BenchmarkUserReadOnlyModelSerializer(c *fiber.Ctx) error {
	// Measure the time it takes to serialize using UserReadOnlyModel
	startTime := time.Now()
	for i := 0; i < 5000; i++ {
		_ = UserModel{
			ID:          1,
			LastLogin:   "2023-09-08T12:34:56",
			IsSuperuser: false,
			Username:    "hakib",
			FirstName:   "haki",
			LastName:    "benita",
			Email:       "me@hakibenita.com",
			IsStaff:     false,
			IsActive:    true,
			DateJoined:  "2023-09-08T12:34:56",
		}
	}
	endTime := time.Now()

	executionTimeMs := endTime.Sub(startTime).Milliseconds()

	return c.JSON(fiber.Map{
		"execution_time_ms": fmt.Sprintf("%d ms", executionTimeMs),
		"data":              createMockUser(),
	})
}

// Define Fiber route handler for UserSerializer benchmark
func BenchmarkUserSerializer(c *fiber.Ctx) error {
	// Measure the time it takes to serialize using UserSerializer
	startTime := time.Now()
	for i := 0; i < 5000; i++ {
		_ = UserModel{
			ID:          1,
			LastLogin:   "2023-09-08T12:34:56",
			IsSuperuser: false,
			Username:    "hakib",
			FirstName:   "haki",
			LastName:    "benita",
			Email:       "me@hakibenita.com",
			IsStaff:     false,
			IsActive:    true,
			DateJoined:  "2023-09-08T12:34:56",
		}
	}
	endTime := time.Now()

	executionTimeMs := endTime.Sub(startTime).Milliseconds()

	return c.JSON(fiber.Map{
		"execution_time_ms": fmt.Sprintf("%d ms", executionTimeMs),
		"data":              createMockUser(),
	})
}

// Helper function to create a mock user
func createMockUser() UserModel {
	return UserModel{
		ID:          1,
		LastLogin:   "2023-09-08T12:34:56",
		IsSuperuser: false,
		Username:    "hakib",
		FirstName:   "haki",
		LastName:    "benita",
		Email:       "me@hakibenita.com",
		IsStaff:     false,
		IsActive:    true,
		DateJoined:  "2023-09-08T12:34:56",
	}
}

func main() {
	app := setupFiberApp()
	err := app.Listen(":3000")
	if err != nil {
		fmt.Printf("Error starting the server: %v", err)
	}
}
