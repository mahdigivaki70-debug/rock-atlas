# TensorFlow Lite uses JNI; keep its Java API intact.
-keep class org.tensorflow.lite.** { *; }
-dontwarn org.tensorflow.lite.gpu.**

# Seed JSON models (kotlinx.serialization ships its own rules; keep ours explicit).
-keep,includedescriptorclasses class ir.rockatlas.data.Seed* { *; }

# Strip verbose logging from release builds.
-assumenosideeffects class android.util.Log {
    public static int v(...);
    public static int d(...);
    public static int i(...);
}
