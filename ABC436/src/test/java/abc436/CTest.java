package abc436;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

class CTest {

    private static String stripLastNewline(String s) {
        // 末尾の改行だけを1個除去（\n / \r\n 対応）
        return s.replaceFirst("\\R\\z", "");
    }

    private static String show(String s) {
        // 見比べやすい表示（改行を可視化）
        return s.replace("\r", "\\\\r").replace("\n", "⏎\\n");
    }


    @Test
    void sample1() {
        String input = "4 3\n1 1\n2 2\n2 3";
        String expected = "2";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            C.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample2() {
        String input = "1000000000 4\n1 1\n1 101\n101 1\n101 101";
        String expected = "4";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            C.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


    @Test
    void sample3() {
        String input = "8 10\n6 5\n7 3\n6 7\n3 4\n4 2\n3 7\n1 3\n7 4\n6 1\n6 1";
        String expected = "8";

        // --- 標準入力を差し替え ---
        ByteArrayInputStream in =
            new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8));
        System.setIn(in);

        // --- 標準出力をキャプチャ ---
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream originalOut = System.out;
        System.setOut(new PrintStream(out));

        try {
            C.main(new String[]{});
        } finally {
            System.setOut(originalOut);
        }

        // main() の出力は「末尾改行だけ」除去して expected と比較
        String resultRaw = out.toString(StandardCharsets.UTF_8);
        String result = stripLastNewline(resultRaw);

        assertEquals(
            expected,
            result,
            "\n--- DIFF ---\n"
            + "expected: [" + show(expected) + "]\n"
            + "result  : [" + show(result) + "]\n"
        );    }


}
